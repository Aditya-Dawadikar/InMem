import React, { useState } from 'react'
import JsonView from '../../components/data/JsonView'
import {MdOutlineContentCopy,
        MdOutlineEdit,
        MdDeleteOutline} from 'react-icons/md'

const DataViewer = () => {
    const [db, set_db] = useState({
        "db_name": "test-db-1",
        "project": "Kanban Board",
        "db_mode": "key-value-store"
    })
    const [docs, set_docs] = useState([
        {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        }, {
            id: "bof3fh2j3fjo3",
        },
    ])

    return (
        <div>
            <div>
                <h3>{db.db_name}</h3>
                <h5>Project: {db.project}</h5>
            </div>
            <div className='row d-flex'>
                <div className='column-fixed-6'>
                    <h4>{
                        db.db_mode === "document-store" ? "Document List" :
                            "Key List"}</h4>
                    <div className='scrollable inset-shadow' style={{ maxHeight: "29em" }}>
                        {
                            docs.map((elem, index) => {
                                return <p
                                    className='document-head'
                                    key={index}>{elem.id}</p>
                            })
                        }
                    </div>
                </div>
                <div className='column-fixed-6'>
                    <div className='d-flex'>
                        <h4>
                            {
                                db.db_mode === "document-store" ?
                                    `Document ID: f3bn93jg3j0g3g0` :
                                    `Key: fb3g939jg0j33g`
                            }
                        </h4>
                        <div className='d-flex' style={{marginLeft: "2em"}}>
                            <div className='icon' style={{margin: "0em 0.2em", cursor: "pointer"}}><MdOutlineContentCopy/></div>
                            <div className='icon' style={{margin: "0em 0.2em", cursor: "pointer"}}><MdOutlineEdit/></div>
                            <div className='icon' style={{margin: "0em 0.2em", cursor: "pointer"}}><MdDeleteOutline/></div>
                        </div>
                    </div>
                    <div className='code'>
                        <div className='scrollable' style={{ maxHeight: "29em" }}>
                            <div style={{ margin: "1em" }}>
                                <JsonView json_data={db}></JsonView>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default DataViewer