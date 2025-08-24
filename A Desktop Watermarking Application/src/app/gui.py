# src/app/gui.py

import customtkinter as ctk
from tkinter import filedialog, colorchooser
from PIL import Image

from core.image_processor import ImageProcessor
from core.watermark_strategies import TextWatermarkStrategy, ImageWatermarkStrategy
from utils.config import ConfigManager


class App(ctk.CTk):
    """
    The main application class for the AquaMark GUI.
    It orchestrates the UI and connects user actions to the core logic.
    """
    
    def __init__(self):
        super().__init__()
        self.title("AquaMark - Professional Watermarking")
        self.geometry("1200x800")
        ctk.set_appearance_mode("dark")
        
        # --- State Variables ---
        self.image_processor: ImageProcessor | None = None
        self.watermark_image_path: str | None = None
        self.text_color = ConfigManager().get("default_text_color")
        self.font_path = ConfigManager().get("default_font_path")
        self.font_size = ConfigManager().get("default_font_size")
        self.display_image: ctk.CTkImage | None = None  # <-- ADD THIS LINE
        
        # --- Layout Configuration ---
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)
        self.grid_rowconfigure(0, weight=1)
        
        # --- UI Initialization ---
        self._create_controls_frame()
        self._create_image_display_frame()
        self._update_ui_state()
    
    # --- UI Creation Methods ---
    
    def _create_controls_frame(self):
        """Creates the left-side frame with all the control widgets."""
        controls_frame = ctk.CTkFrame(self, width=300)
        controls_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        controls_frame.grid_propagate(False)
        
        # --- File Controls ---
        file_label = ctk.CTkLabel(controls_frame, text="1. Load Image", font=ctk.CTkFont(weight="bold"))
        file_label.pack(pady=(10, 5), padx=10, fill="x")
        
        self.load_image_btn = ctk.CTkButton(controls_frame, text="Load Base Image", command=self._load_base_image)
        self.load_image_btn.pack(pady=5, padx=10, fill="x")
        
        # --- Watermark Type Tabs ---
        self.tab_view = ctk.CTkTabview(controls_frame)
        self.tab_view.pack(pady=10, padx=10, fill="x")
        self.tab_view.add("Text Watermark")
        self.tab_view.add("Image Watermark")
        self._create_text_watermark_tab(self.tab_view.tab("Text Watermark"))
        self._create_image_watermark_tab(self.tab_view.tab("Image Watermark"))
        
        # --- Common Settings ---
        settings_label = ctk.CTkLabel(controls_frame, text="2. Adjust Settings", font=ctk.CTkFont(weight="bold"))
        settings_label.pack(pady=(10, 5), padx=10, fill="x")
        
        # Opacity Slider
        opacity_frame = ctk.CTkFrame(controls_frame, fg_color="transparent")
        opacity_frame.pack(fill="x", padx=10, pady=5)
        ctk.CTkLabel(opacity_frame, text="Opacity:").pack(side="left")
        self.opacity_slider = ctk.CTkSlider(opacity_frame, from_=0, to=1, command=self._preview_watermark)
        self.opacity_slider.set(ConfigManager().get("default_opacity"))
        self.opacity_slider.pack(side="left", fill="x", expand=True, padx=10)
        
        # Position Radio Buttons
        ctk.CTkLabel(controls_frame, text="Position:").pack(padx=10, anchor="w")
        self.position_var = ctk.StringVar(value=ConfigManager().get("default_position"))
        position_frame = ctk.CTkFrame(controls_frame)
        position_frame.pack(fill="x", padx=10, pady=5)
        positions = [
            ("top_left", "TL"), ("top_center", "TC"), ("top_right", "TR"),
            ("center_left", "CL"), ("center", "C"), ("center_right", "CR"),
            ("bottom_left", "BL"), ("bottom_center", "BC"), ("bottom_right", "BR")
        ]
        for i, (key, text) in enumerate(positions):
            ctk.CTkRadioButton(
                position_frame, text=text, variable=self.position_var, value=key,
                command=self._preview_watermark, width=40
            ).grid(row=i // 3, column=i % 3, padx=5, pady=5)
        
        # --- Actions ---
        actions_label = ctk.CTkLabel(controls_frame, text="3. Save Image", font=ctk.CTkFont(weight="bold"))
        actions_label.pack(pady=(20, 5), padx=10, fill="x")
        
        self.save_btn = ctk.CTkButton(controls_frame, text="Save Watermarked Image", command=self._save_image)
        self.save_btn.pack(pady=10, padx=10, fill="x")
    
    def _create_text_watermark_tab(self, tab):
        """Creates controls for the text watermark tab."""
        ctk.CTkLabel(tab, text="Watermark Text:").pack(padx=5, anchor="w")
        self.text_entry = ctk.CTkEntry(tab, placeholder_text="Enter watermark text...")
        self.text_entry.pack(fill="x", padx=5, pady=5)
        self.text_entry.bind("<KeyRelease>", self._preview_watermark)
        
        color_btn = ctk.CTkButton(tab, text="Choose Color", command=self._choose_color)
        color_btn.pack(fill="x", padx=5, pady=5)
    
    def _create_image_watermark_tab(self, tab):
        """Creates controls for the image watermark tab."""
        self.load_watermark_btn = ctk.CTkButton(tab, text="Load Watermark Image", command=self._load_watermark_image)
        self.load_watermark_btn.pack(fill="x", padx=5, pady=10)
        self.watermark_path_label = ctk.CTkLabel(tab, text="No image loaded.", wraplength=250)
        self.watermark_path_label.pack(fill="x", padx=5)
        
        # Scale Slider
        scale_frame = ctk.CTkFrame(tab, fg_color="transparent")
        scale_frame.pack(fill="x", padx=5, pady=10)
        ctk.CTkLabel(scale_frame, text="Scale:").pack(side="left")
        self.scale_slider = ctk.CTkSlider(scale_frame, from_=0.1, to=1.0, command=self._preview_watermark)
        self.scale_slider.set(0.3)
        self.scale_slider.pack(side="left", fill="x", expand=True, padx=10)
    
    def _create_image_display_frame(self):
        """Creates the right-side frame for displaying the image."""
        self.image_frame = ctk.CTkFrame(self)
        self.image_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.image_label = ctk.CTkLabel(self.image_frame, text="Load an image to begin", text_color="gray")
        self.image_label.pack(expand=True)
    
    # --- UI Callbacks and Logic ---
    
    def _load_base_image(self):
        """Opens a file dialog to load the base image."""
        file_path = filedialog.askopenfilename(
            title="Select a Base Image",
            filetypes=(("Image files", "*.jpg *.jpeg *.png *.bmp"), ("All files", "*.*"))
        )
        if file_path:
            self.image_processor = ImageProcessor(file_path)
            self._display_image(self.image_processor.original_image)
            self._update_ui_state()
            self._preview_watermark()
    
    def _load_watermark_image(self):
        """Opens a file dialog to load the watermark image."""
        file_path = filedialog.askopenfilename(
            title="Select a Watermark Image",
            filetypes=(("PNG files", "*.png"), ("All files", "*.*"))
        )
        if file_path:
            self.watermark_image_path = file_path
            self.watermark_path_label.configure(text=file_path.split('/')[-1])
            self._preview_watermark()
    
    def _choose_color(self):
        """Opens a color chooser dialog for the text watermark."""
        color_code = colorchooser.askcolor(title="Choose color")
        if color_code and color_code[1]:
            self.text_color = color_code[1]
            self._preview_watermark()
    
    def _preview_watermark(self, _=None):
        """Updates the image preview by applying the current watermark settings."""
        if not self.image_processor:
            return
        
        current_tab = self.tab_view.get()
        strategy = None
        
        if current_tab == "Text Watermark":
            text = self.text_entry.get()
            if not text:
                self._display_image(self.image_processor.original_image)
                return
            strategy = TextWatermarkStrategy(
                text=text,
                font_path=self.font_path,
                font_size=self.font_size,
                color=self.text_color,
                position=self.position_var.get(),
                opacity=self.opacity_slider.get()
            )
        elif current_tab == "Image Watermark":
            if not self.watermark_image_path:
                self._display_image(self.image_processor.original_image)
                return
            strategy = ImageWatermarkStrategy(
                watermark_path=self.watermark_image_path,
                position=self.position_var.get(),
                opacity=self.opacity_slider.get(),
                scale=self.scale_slider.get()
            )
        
        if strategy:
            self.image_processor.apply_watermark(strategy)
            self._display_image(self.image_processor.processed_image)
    
    def _save_image(self):
        """Saves the watermarked image to a file."""
        if self.image_processor and self.image_processor.processed_image:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*"))
            )
            if file_path:
                self.image_processor.save_image(file_path)
    
    def _display_image(self, pil_image: Image.Image):
        """Displays a PIL image in the image_label widget."""
        frame_w = self.image_frame.winfo_width()
        frame_h = self.image_frame.winfo_height()
        
        # Avoid division by zero if frame not rendered yet
        if frame_w < 2 or frame_h < 2:
            self.after(50, lambda: self._display_image(pil_image))
            return
        
        img_copy = pil_image.copy()
        img_copy.thumbnail((frame_w - 20, frame_h - 20), Image.Resampling.LANCZOS)
        
        ctk_image = ctk.CTkImage(light_image=img_copy, dark_image=img_copy, size=img_copy.size)
        self.image_label.configure(image=ctk_image, text="")
    
    def _update_ui_state(self):
        """Enables or disables UI elements based on the application state."""
        has_image = self.image_processor is not None
        self.save_btn.configure(state="normal" if has_image else "disabled")
        for widget in [self.opacity_slider, self.position_var, self.tab_view]:
            if hasattr(widget, 'configure'):
                widget.configure(state="normal" if has_image else "disabled")