import GET_ERRORS from '../actions/types';

const initialState = {
  data: 'ttvtv'
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_ERRORS:
      return {
        ...state,
        data: action.payload
      };
    default:
      return state;
  }
}
