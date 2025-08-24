Build Your Own Spotify Wrapped
=================================

Ever wondered what your Spotify stats would look like beyond the official "Wrapped" slideshow? This Jupyter Notebook provides a step-by-step guide to dive deep into your personal Spotify listening history and uncover unique insights about your habits.

Using your own extended streaming history data, this project helps you answer questions like:

-   What songs did I listen to on the most consecutive days?

-   Which tracks were my most consistent companions throughout the year?

-   How many hours did I *really* spend listening to my favorite artists?

Features & Analysis
-------------------

This notebook walks you through performing several custom analyses on your listening data:

-   ** Longest Listening Streaks:** Discover which songs you played on the most consecutive days in a given year. Perfect for identifying your binge-worthy tracks and daily anthems.

-   ** Most Consistent Tracks:** Find out which songs you listened to on the highest number of *distinct days* throughout the year, revealing your true long-term favorites.

-   **️ Total Playtime Calculation:** Quantify your listening time by calculating the total hours played for each song.

-   ** Year-over-Year Comparison:** The code is structured to easily filter and analyze your habits for any year present in your data.

How It Works
------------

The notebook follows a clear, multi-step process:

1.  **Data Loading & Preparation:** Your Spotify streaming history files are loaded into a single, manageable `pandas` DataFrame.

2.  **Initial Cleaning:** Timestamps are converted into a proper datetime format, and essential columns like `year` and `date` are extracted for easier filtering and analysis.

3.  **Defining Streaks (e.g., for 2024):**

    -   The dataset is filtered for a specific year.

    -   Duplicate plays on the same day are removed to ensure each song is counted only once per day.

    -   A custom function iterates through the listening dates for each song to find the longest streak of consecutive days it was played.

    -   The results are merged with total playtime data and displayed.

4.  **Analyzing Consistency (e.g., for 2023):**

    -   The data is filtered for another year.

    -   The notebook calculates the total number of unique days each song was played.

    -   This metric is combined with total playtime to create a comprehensive view of your most frequently heard tracks.

    -   The final table is sorted to show the top 10 most consistently played songs.

Getting Started
---------------

You can run this analysis on your own Spotify data by following these steps.

### Prerequisites

-   Python 3.x

-   Jupyter Notebook or JupyterLab

-   The `pandas` library (`pip install pandas`)

### 1\. Request Your Spotify Data

You need your "Extended streaming history" data from Spotify.

1.  Go to Spotify's **[Privacy Settings](https://www.spotify.com/us/account/privacy/)** page and log in.

2.  Scroll down to the **"Download your data"** section.

3.  Select the **"Extended streaming history"** option.

4.  Follow the instructions to submit your request.

> **Note:** It can take Spotify several days (sometimes up to 30) to prepare your data. They will email you a link to download a `.zip` file when it's ready.

### 2\. Set Up the Project

1.  Clone or download this repository.

2.  Unzip your downloaded Spotify data and place the `Streaming_History_Audio_... .json` files into the same directory as the notebook, or into a dedicated `data/` subfolder.

3.  Make sure you have `pandas` installed:

    Bash

    ```
    pip install pandas

    ```

### 3\. Run the Notebook

1.  Launch Jupyter Notebook or JupyterLab from your terminal:

    Bash

    ```
    jupyter notebook

    ```

2.  Open the `.ipynb` file.

3.  Adjust the file path in the data loading cell to match where you placed your `.json` files.

4.  Run the cells in order to see your personalized Spotify Wrapped!