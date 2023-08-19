import React, { useState, useEffect } from 'react'
import DATATYPE_OPTION_MAP from './DataTypeOptions'

import { MdAdd, MdDeleteOutline } from 'react-icons/md'

const CreateSchema = () => {
    const [formElements, setFormElements] = useState([
        {
            "field_name": "",
            "field_type": "string",
            "allow_null": true
        }
    ])

    useEffect(() => {
        console.log(formElements)
    }, [formElements])

    function handleAddFormElement() {
        let newFormElementList = [...formElements]
        newFormElementList.push({
            "field_name": "",
            "field_type": "string",
            "allow_null": true
        })
        setFormElements(newFormElementList)
    }

    function handleRemoveFromElement(index) {
        let newFormElementList = formElements.filter((_, i) => i !== index);

        if (newFormElementList.length === 0) {
            newFormElementList.push({
                "field_name": "",
                "field_type": "string",
                "allow_null": true
            })
        }
        setFormElements(newFormElementList);
    }

    function handleFormFieldChange(index, fieldname, value) {
        const newFormElementList = formElements.map((formElem, i) => {
            if (i == index) {
                return { ...formElem, [fieldname]: value }
            }
            return formElem
        })
        setFormElements(newFormElementList)
    }

    function AddField() {
        return <div >
            <div
                className='add-btn'
                onClick={() => {
                    handleAddFormElement()
                }} >
                <MdAdd />
            </div>
        </div>
    }

    return (
        <div>
            {
                formElements.map((formElem, index) => {
                    return <div key={index} style={{
                        margin: "0.2em"
                    }}>
                        <div>
                            <input
                                placeholder='Field Name'
                                onChange={(e) => {
                                    handleFormFieldChange(index,
                                        "field_name",
                                        e.target.value)
                                }}
                                value={formElem.field_name}
                            ></input>
                            <select
                                value={formElem.field_type}
                                onChange={(e) => {
                                    handleFormFieldChange(index,
                                        "field_type",
                                        e.target.value)
                                }}
                            >
                                {
                                    DATATYPE_OPTION_MAP.map((datatype, datatype_index) => {
                                        return <option
                                            key={datatype_index}
                                            value={datatype.type}>{datatype.type.toUpperCase()}</option>
                                    })
                                }
                            </select>
                            <MdDeleteOutline
                                style={{
                                    marginLeft: "0.2em",
                                    position: "relative",
                                    top: "0.2em",
                                    cursor: "pointer"
                                }}

                                onClick={() => {
                                    handleRemoveFromElement(index)
                                }}
                            />
                        </div>
                        <div>
                            <div>
                                {/* TODO: Containts Handling Code goes here */}
                            </div>
                            {
                                formElem.datatype === "object" || formElem.datatype === "array" ?
                                    <div>
                                        {/* TODO: Nested Input Handling Code goes here */}
                                    </div> :
                                    <></>
                            }
                        </div>
                        <hr />
                    </div>
                })
            }
            <AddField />
        </div>
    )
}

export default CreateSchema