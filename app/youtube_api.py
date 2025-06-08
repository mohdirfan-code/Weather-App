import requests
import os

def search_youtube_videos(query, api_key=None, max_results=3):
    """
    Search YouTube for embeddable, public weather-related videos with thumbnails.
    Returns up to max_results (may be fewer).
    """
    if not api_key:
        api_key = os.getenv("YOUTUBE_API_KEY")
    search_url = "https://www.googleapis.com/youtube/v3/search"
    query = f"{query} weather"
    params = {
        "q": query,
        "part": "snippet",
        "type": "video",
        "videoEmbeddable": "true",
        "safeSearch": "strict",
        "key": api_key,
        "maxResults": max_results * 4,  # over-fetch for better filtering
    }
    resp = requests.get(search_url, params=params, timeout=10)
    resp.raise_for_status()
    items = resp.json().get("items", [])
    video_ids = [item["id"]["videoId"] for item in items if "id" in item and "videoId" in item["id"]]

    if not video_ids:
        return []

    # Get video details (status, snippet, thumbnails)
    videos_url = "https://www.googleapis.com/youtube/v3/videos"
    check_params = {
        "id": ",".join(video_ids),
        "part": "snippet,status",
        "key": api_key,
    }
    resp2 = requests.get(videos_url, params=check_params, timeout=10)
    resp2.raise_for_status()
    video_items = resp2.json().get("items", [])

    results = []
    for item in video_items:
        vid = item["id"]
        snippet = item.get("snippet", {})
        status = item.get("status", {})
        title = snippet.get("title")
        # Use medium quality thumbnail if available
        thumbnail = snippet.get("thumbnails", {}).get("medium", {}).get("url") \
            or snippet.get("thumbnails", {}).get("default", {}).get("url")

        # Only use public, embeddable, and has a thumbnail
        if status.get("embeddable") and status.get("privacyStatus") == "public" and thumbnail:
            results.append({
                "videoId": vid,
                "title": title,
                "thumbnail": thumbnail
            })
            if len(results) >= max_results:
                break
    return results