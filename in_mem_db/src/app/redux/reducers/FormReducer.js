import { FormHandlerConstants } from "../constants/FormHandlers"

const FormReducer = (state={}, action)=>{
    switch(action.type){
        case FormHandlerConstants.OPEN_FORM:
            return {...state, show: action.payload.show}
        case FormHandlerConstants.CLOSE_FORM:
            return {...state, show: action.payload.show}
        default:
            return state
    }
}

export default FormReducer