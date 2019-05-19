import { actionTypes } from '../actions/actions';

const initialState = {
  tracks: [],
  activeTrack: {
    key: '00000000',
    title: 'No Track Playing',
    text: 'Article text',
    image: 'Null',
    percent: '0.0',
    audio: 'None',
  },
};

export default function tracksReducer(state = initialState, action) {
  switch (action.type) {
    case actionTypes.LOAD_TRACKS:
      return {
        ...state,
        tracks: action.tracks,
      };
    case actionTypes.SELECTED_TRACK:
      return {
        ...state,
        activeTrack: action.track,
      };
    default:
      return state;
  }
};
