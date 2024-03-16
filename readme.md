## Prerequisites

Before running the application, ensure you have the following:

- Python 3.x installed
- MongoDB installed and configured
- Access token for the Facebook Graph API with necessary permissions (pages_read_engagement, pages_read_user_content, pages_show_list).

### Obtaining a Facebook Graph API Access Token

To use the Facebook Graph API, you need an access token with the necessary permissions. Follow these steps to obtain an access token:

1. Create a Facebook App:
    - Go to the [Facebook Developers](https://developers.facebook.com/) website and create a new app.
    - Note down the App ID and App Secret.

2. Obtain User Access Token:
    - Visit the [Facebook Graph API Explorer](https://developers.facebook.com/tools/explorer/) tool.
    - Select your app from the "Application" dropdown menu.
    - Click on "Get Token" and select "Get User Access Token".
    - Grant necessary permissions (e.g., pages_read_engagement, pages_read_user_content, pages_show_list).
    - Click "Generate Access Token" and copy the generated token.

3. Replace Access Token in `main.py`:
    - Open `main.py` in your project directory.
    - Replace the `ACCESS_TOKEN` variable with the generated access token.

## Getting Started

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/dhouh/scrapapp.git
    ```

2. Install dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up MongoDB:
    - Install MongoDB and start the MongoDB service.
    - Configure the MongoDB connection directly in `main.py`

4. Update the `ACCESS_TOKEN` and `PAGE_ID` variables in `main.py` with your Facebook page ID and access token.

5. Run the application:

    ```bash
    uvicorn main:app --reload
    ```

## Running Tests

To run the unit tests for this application, follow these steps:


1. Run the tests using the following command:

    ```bash
    python -m unittest
    ```

This command will discover and execute all test cases within the `tests` directory.

## Coverage

To generate a coverage report for the tests, you can use the `coverage` tool. First, ensure that `coverage` is installed:

```bash
pip install coverage


## Usage

- Access the web service by navigating to `http://localhost:8000` in your web browser.
- To retrieve Facebook posts, make a GET request to `/posts/`.

## Dockerization

If you prefer to use Docker Compose to manage your application and its dependencies, you can use the provided `docker-compose.yml` file.

1. Ensure that Docker Compose is installed on your system.

2. Modify the `docker-compose.yml` file to configure any necessary environment variables or volumes.

3. Run the following command to start the application:

    ```bash
    docker-compose up -d
    ```

This command will build and start the Docker containers defined in the `docker-compose.yml` file in detached mode.

To stop the containers, run:

```bash
docker-compose down
    ```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).