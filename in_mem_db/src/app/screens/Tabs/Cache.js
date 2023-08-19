import React, { useState } from 'react'

const Cache = () => {
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
        }
    ])
    return (
        <div style={{ "height": "inherit" }}>
            <div>
                <h4>Cache Metrics</h4>
                <div className='d-flex'>
                    <div className='kpi-tile shadow'>
                        <h1 className='kpi-detail'>0.83</h1>
                        <h4 className='kpi-meta'>Hit Ratio</h4>
                    </div>
                    <div className='kpi-tile shadow'>
                        <h1 className='kpi-detail'>0.17</h1>
                        <h4 className='kpi-meta'>Miss Ratio</h4>
                    </div>
                    <div className='kpi-tile shadow'>
                        <h1 className='kpi-detail'>82</h1>
                        <h4 className='kpi-meta'>Cached Items</h4>
                    </div>
                </div>
            </div>
            <br />
            <div>
                <h4>Cache Contents</h4>
                <div className='row d-flex'>
                    <div className='column-fixed-6'>
                        <h4>Documents</h4>
                        <div className='scrollable inset-shadow' style={{ maxHeight: "21em" }}>
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
                        <h4>id: fn3ohwojf3j0gh329gh3</h4>
                        <div className='code'>
                            <div className='scrollable' style={{ maxHeight: "21em" }}>
                                <div style={{margin:"1em"}}>
                                    {
                                        docs.map((elem, index) => {
                                            return <p
                                                key={index}>{elem.id}</p>
                                        })
                                    }
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Cache