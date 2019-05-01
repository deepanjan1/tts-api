import { actionTypes } from '../actions/actions';

const initialState = {
  tracks: [],
  activeTrack: 'Nothing is Playing',
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
