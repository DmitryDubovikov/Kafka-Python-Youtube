import logging
import os
import requests
import json
from dotenv import load_dotenv


logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    logging.info("START")

    load_dotenv()
    google_api_key = os.environ["GOOGLE_API_KEY"]
    youtube_playlist_id = os.environ["YOUTUBE_PLAYLIST_ID"]

    response = requests.get(
        "https://www.googleapis.com/youtube/v3/playlistItems",
        params={
            "key": google_api_key,
            "playlistId": youtube_playlist_id,
            # "part": "contentDetails",
            # "pageToken": page_token,
        },
    )

    payload = json.loads(response.text)

    logging.info(f"GOT {payload}")


if __name__ == "__main__":
    main()
