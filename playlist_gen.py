def search_youtube(client, search_phrase, count=1):
  """Returns the top video id for a keyword (search phrase)
  param: search_phrase, string: Youtube search term
  param: count, int, optional: Number of ids to return
  return: list of video IDs
  """

  # using the youtube api, search for your video using the keyword
  # API Function documentation - https://developers.google.com/youtube/v3/docs/search/list 
  # ToDo: Fill the search function with the proper paramaters (ex: q, type, etc.)
  search_result = client.search().list(
    # fill in here
  ).execute()

  # initialize empty list to store video IDs in
  video_list =[]

  # for loop until we hit our desired video count
  for i in range(count):
    # add the video id to the list
    video_list.append(search_result['items'][i]['id']['videoId'])

  # return the list of video IDs 
  return video_list

def create_youtube_links(video_ids):
  """Returns a list of youtube links for given video ids
  param: video_ids, list: List of Youtube video IDs to generate links for
  return: list: List of Youtube video web links
  """
  
  # todo: initalize empty list called links to store youtube video links in

  # todo: loop through the list of provided video ids (video_ids)

    # todo: create a web link string (format is: 'https://youtu.be/videoID'), and append it to our links list

  # todo: return the list of youtube video web links

def create_playlist(client, playlist_name, playlist_description=''):
  """Creates an empty playlist.
  param: client: The YouTube API object.
  param: playlist_name: The name of our playlist.
  param: playlist_description: An optional description for our playlist.
  return: The playlist ID of our newly-created playlist.
  """

  # Create the playlist first.
  # We have to format our request with a dictionary like the ones shown in the documentation.
  # See: https://developers.google.com/youtube/v3/docs/playlists/insert
  create_playlist_request_body = {
    # TODO: Add the snippet and the status fields to the request body!
  }
  # Call the insert operation on the YouTube API, using the request object we just created.
  # See: https://developers.google.com/youtube/v3/docs/playlists/insert
  create_playlist_response = client.playlists().insert(
    part='snippet,status',
    body=create_playlist_request_body
  ).execute()

  # The code above only creates the playlist.
  # If you have videos to add to the playlist, remember to do that with `insert_videos_into_playlist`!

  # If all goes well, there should be no errors, and our requests were successful.
  # TODO: Return the playlist ID.

def insert_videos_into_playlist(client, playlist_id, video_ids=[]):
  """Inserts videos into an existing playlist.
  param: playlist_id, string: The playlist ID of the playlist we want to add into.
  param: video_ids, list: An optional list of video IDs (strings) that we want to put in the playlist.
  return: None
  """

  # Loop through the list of videos we want to add.
  for video_id in video_ids:
    # For each individual video ID, create another request object for the API to consume.
    # See: https://developers.google.com/youtube/v3/docs/playlistItems/insert
    insert_video_request_body = {
      # TODO: Add the video snippet!
    }
    # Call the insert operation on the YouTube API, using the request object we just created.
    # See: https://developers.google.com/youtube/v3/docs/playlistItems/insert
    insert_video_response = client.playlistItems().insert(
      part='snippet',
      body=insert_video_request_body
    ).execute()


  # If all goes well, there should be no errors, and our requests were successful.
  return
