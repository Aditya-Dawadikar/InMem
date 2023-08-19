import React from 'react'

import {useDispatch} from 'react-redux'

import {closeForm} from '../../redux/actions/FormActions' 

import { AiOutlineCloseCircle } from 'react-icons/ai'

const CreateDBForm = () => {

    const dispatch = useDispatch()

    function handleFormClose() {
        dispatch(closeForm())
    }

    function handleSave() {
        dispatch(closeForm())
    }

    return (
        <>
            <div
                className='close-btn'
                onClick={() => {
                    handleFormClose()
                }}>
                <AiOutlineCloseCircle />
            </div>
            <div className='row' style={{ justifyContent: 'center' }}>
                <h3>Create New Database</h3>
            </div>
            <br />
            <div className='row'>
                <div className='column' style={{ padding: '0' }}>
                    <label>Database Name</label>
                    <br />
                    <input placeholder='My First DB'></input>
                </div>
                <div className='column' style={{ padding: '0' }}>
                    <label>Database Mode</label>
                    <br />
                    <select>
                        <option value="key-value-store">Key-Value Store</option>
                        <option value="document-store">Document Store</option>
                    </select>
                </div>
            </div>
            <br />
            {/* 
            
                TODO: To be added when schema enforcement feature is available
            
            <div className='row'>
                <div className='column' style={{ padding: '0' }}>
                    <label>Enforce Schema?</label>
                    <div className='d-flex'>
                        <div style={{ marginLeft: "0.5em" }}>
                            <label>Yes</label>
                            <input type='radio'></input>
                        </div>
                        <div style={{ marginLeft: "0.5em" }}>
                            <label>No</label>
                            <input type='radio'></input>
                        </div>
                    </div>
                </div>
            </div>

            */}

            <br />
            <div className='row'>
                <div className='column' style={{ padding: '0' }}>
                    <label>App Name</label>
                    <br />
                    <input placeholder='My first app'></input>
                </div>
            </div>
            <br />
            {/* 
                TODO: TO Be added when User support is added
            
            <div className='row'>
                <div className='column' style={{ padding: '0' }}>
                    <label>Add Users</label>
                    <br />
                    <div className='d-flex'>
                        <input type='email' value='johndoe@inmemdb.com'></input>
                        <button className='btn'>+</button>
                    </div>
                </div>
                <br />
                <div className='column' style={{ padding: '0' }}>
                    <label>Current Users</label>
                    <br />
                    <ul className='inset-shadow scrollable'
                        style={{
                            padding: "0.2em",
                            margin: "0",
                            maxHeight: "5em"
                        }}>
                        <li className='d-flex document-head' style={{ margin: "0", padding: "0.2em" }}>
                            <div>johndoe1@inmemdb.com</div>
                            <div className='icon'><MdDeleteOutline /></div>
                        </li>
                        <li className='d-flex document-head' style={{ margin: "0", padding: "0.2em" }}>
                            <div>johndoe2@inmemdb.com</div>
                            <div className='icon'><MdDeleteOutline /></div>
                        </li>
                        <li className='d-flex document-head' style={{ margin: "0", padding: "0.2em" }}>
                            <div>johndoe3@inmemdb.com</div>
                            <div className='icon'><MdDeleteOutline /></div>
                        </li>
                    </ul>
                </div>
            </div> */
            
            }
            <br /><br />
            <div className='row' style={{ justifyContent: 'center' }}>
                <div
                    className='btn'
                    onClick={() => {
                        handleSave()
                    }}>Create DB</div>
            </div>
        </>
    )
}

export default CreateDBForm