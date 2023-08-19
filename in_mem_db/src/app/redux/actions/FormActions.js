import { FormHandlerConstants } from "../constants/FormHandlers"

export const openForm = ()=> async(dispatch)=>{
    try{
        dispatch({
            type: FormHandlerConstants.OPEN_FORM,
            payload: {
                show: true
            }
        })
    }catch(error){
        console.log(error)
    }
}

export const closeForm = ()=> async(dispatch)=>{
    try{
        dispatch({
            type: FormHandlerConstants.CLOSE_FORM,
            payload: {
                show: false
            }
        })
    }catch(error){
        console.log(error)
    }
}
