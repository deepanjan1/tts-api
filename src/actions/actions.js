
export const actionTypes = {
  LOAD_TRACKS: 'LOAD_TRACKS',
  SELECTED_TRACK: 'SELECTED_TRACK',
};

// function to make API call and pull track data (CAN REFACTOR)
export const trackListData = () => (dispatch) =>
  {
    fetch('http://localhost:5000/tracks').then(
      (response) => response.json())
      .then((res) => dispatch(loadTracks(res)));
  };

export const loadTracks = (tracks) => (dispatch) => (
  dispatch({
    type: 'LOAD_TRACKS',
    tracks,
  })
);

export const selectedTrack = (track) => (dispatch) => (
  dispatch({
    type: 'SELECTED_TRACK',
    track,
  })
);
