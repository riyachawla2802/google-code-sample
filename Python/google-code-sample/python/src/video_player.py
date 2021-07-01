"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
from .video import Video
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.currently_playing = None
        self.pause = False
        self.playlists = dict()
        self.playlist_names = dict()

# --------------------------- PART 1 -------------------------------
    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all available videos:")
        all_videos = self._video_library.get_all_videos()
        all_videos_sorted = sorted(all_videos, key=lambda video: video.title)

        for video in all_videos_sorted:
            print(
                f"  {video._title} ({video._video_id}) [{' '.join(list(video._tags))}]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        all_videos = self._video_library.get_all_videos()
        all_video_ids = []
        for video in all_videos:
            all_video_ids.append(video._video_id)

        if video_id in all_video_ids:

            if self.currently_playing is not None:
                print(f"Stopping video: {self.currently_playing._title}")
                self.currently_playing = None

            if self.currently_playing is None:
                print(
                    f"Playing video: {self._video_library.get_video(video_id)._title}")
                self.currently_playing = self._video_library.get_video(
                    video_id)
                self.pause = False
        else:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""

        if self.currently_playing is not None:
            print(f"Stopping video: {self.currently_playing._title}")
            self.currently_playing = None
            self.pause = False
        else:
            print("Cannot stop video: No video is currently playing.")

    def play_random_video(self):
        """Plays a random video from the video library."""

        random_number = random.randint(
            0, len(self._video_library.get_all_videos()))
        all_videos = self._video_library.get_all_videos()
        if self.currently_playing != None:
            print(f"Stopping video: {self.currently_playing._title}")
            self.currently_playing = None

        if self.currently_playing == None:
            print(f"Playing video: {all_videos[random_number]._title}")
            self.currently_playing = all_videos[random_number]._title
            self.pause = False

    def pause_video(self):
        """Pauses the current video."""

        if self.currently_playing is None:
            print("Cannot pause video: No video is currently playing")
        else:
            if self.pause is False:
                print(f"Pausing video: {self.currently_playing._title}")
                self.pause = True

            elif self.pause is True:
                print(
                    f"Video already paused: {self.currently_playing._title}")

    def continue_video(self):
        """Resumes playing the current video."""

        if self.currently_playing is None:
            print("Cannot continue video: No video is currently playing")
        else:
            if self.pause is False:
                print("Cannot continue video: Video is not paused")
            elif self.pause is True:
                print(f"Continuing video: {self.currently_playing._title}")
                self.pause = False

    def show_playing(self):
        """Displays video currently playing."""

        if self.currently_playing is None:
            print("No video is currently playing")
        else:
            print(
                f"Currently playing: {self.currently_playing._title} ({self.currently_playing._video_id}) [{' '.join(list(self.currently_playing._tags))}]", end="")
            if self.pause is True:
                print(" - PAUSED")

# --------------------------- PART 2 ---------------------------------------

    def playlist_exists(self, name):
        return name in self.playlists.keys()

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        name_of_playlist = playlist_name.lower()

        if name_of_playlist in self.playlists.keys():
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self.playlists[name_of_playlist] = []
            self.playlist_names[name_of_playlist] = playlist_name
            print(
                f"Successfully created new playlist: {self.playlist_names[name_of_playlist]}")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        name_of_playlist = playlist_name.lower()
        video = self._video_library.get_video(video_id)

        if self.playlist_exists(name_of_playlist):

            if video != None:
                if(video.flagged == None):
                    if video in self.playlists[name_of_playlist]:
                        print("Cannot add video to " +
                              playlist_name + ": Video already added")
                    else:
                        self.playlists[name_of_playlist].append(video)
                        print("Added video to " +
                              playlist_name + ":", video._title)
                else:
                    print("Cannot add video to " + playlist_name + ": Video is currently flagged (reason: " +
                          video.flagged + ")")
            else:
                print("Cannot add video to " +
                      playlist_name + ": Video does not exist")

        else:
            print("Cannot add video to " + playlist_name +
                  ": Playlist does not exist")

    def show_all_playlists(self):
        """Display all playlists."""

        if len(self.playlists.keys()) == 0:
            print("No playlists exist yet")
        else:
            print("Showing all playlists: ")
            for playlist in sorted(self.playlists.keys()):
                print("  " + self.playlist_names[playlist.lower()])

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

# ---------------------------------- PART 3 ----------------------------

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
