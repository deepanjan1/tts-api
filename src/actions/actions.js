// import {
//   getReminders,
//   contactListener,
//   currentUserListener,
//   getPermissions,
// } from '../services/api';

export const actionTypes = {
  LOAD_TRACKS: 'LOAD_TRACKS',
  SELECTED_TRACK: 'SELECTED_TRACK',
};

// Get Track Stuff
const listData = [
  {
    key: 'Article 1',
    percent: 0.2,
    image: 'https://facebook.github.io/react-native/docs/assets/favicon.png',
  },
  {
    key: 'Article 2',
    percent: 0.4,
    image: 'https://facebook.github.io/react-native/docs/assets/favicon.png',
  },
  {
    key: 'Article 3',
    percent: 0.4,
    image: 'https://facebook.github.io/react-native/docs/assets/favicon.png',
  },
  {
    key: 'Article 4',
    percent: 0.4,
    image: 'https://facebook.github.io/react-native/docs/assets/favicon.png',
  },
  {
    key: 'Article 5',
    percent: 0.4,
    image: 'https://facebook.github.io/react-native/docs/assets/favicon.png',
  },
  {
    key: 'Article 6',
    percent: 0.4,
    image: 'https://facebook.github.io/react-native/docs/assets/favicon.png',
  },
  {
    key: 'Article 7',
    percent: 0.4,
    image: 'https://facebook.github.io/react-native/docs/assets/favicon.png',
  },
  {
    key: 'Article 8',
    percent: 0.7,
    image: 'https://facebook.github.io/react-native/docs/assets/favicon.png',
  },
  {
    key: 'Article 9',
    percent: 0.7,
    image: 'https://facebook.github.io/react-native/docs/assets/favicon.png',
  },
];

// function to make API call and pull track data
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
