# asteroid-tracker

This Python script fetches information on near-Earth asteroids within a specified date range using NASA's Near Earth Object Web Service (NeoWs). NeoWs is a RESTful web service for near earth Asteroid information.

My CLI application takes the `start_date` and `end_date` as arguments and outputs the name, Asteroid ID as well as NEO Refernce ID of the asteroid(s) within the specified date range.

It also takes optional arguments `-s` or `--size` that gives us information about the asteroid's size and the `-d` or the `--distance` optional argument that outputs the information on distance bwteween the Earth and the Asteroid.



## Prerequisites

- Python 3.x
- Access to the internet

## Setup

1. **Clone the repository**

    Clone the repository to your local machine.

    ```bash
    git clone <repository_url>
    ```

2. **Navigate to the cloned directory**

    Change your current directory to the directory containing the script.

    ```bash
    cd <directory_path>
    ```

3. **Set up the environment variable**

    The script uses an environment variable `ASTEROIDS_API` to store the API key. You need to set this environment variable in your system.

    - On Unix or Linux:

        ```bash
        export ASTEROIDS_API=your_api_key
        ```

    - On Windows:

        ```cmd
        setx ASTEROIDS_API "your_api_key"
        ```

    Replace `your_api_key` with your actual API key.

## Usage

Run the script with the start and end dates as arguments. You can also use the `-s` flag to display the size of the asteroids and the `-d` flag to display the distance of the asteroids from Earth.

```bash
python asteroids.py start_date end_date -s -d
