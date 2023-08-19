import {createStore, applyMiddleware, combineReducers} from 'redux'
import thunk from 'redux-thunk'
import logger from 'redux-logger'

import FormReducer from './reducers/FormReducer'

const rootReducer = combineReducers({
    form: FormReducer
})

const store = createStore(rootReducer, applyMiddleware(thunk, logger))

export default store