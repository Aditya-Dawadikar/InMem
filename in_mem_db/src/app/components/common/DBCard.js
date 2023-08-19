import React from 'react'
import { useNavigate } from 'react-router-dom'

const DBCard = (props) => {
    const navigate = useNavigate()

    function handleGetStarted(url){
        navigate(`/workbench/${url}`)
    }

    return (
        <div className='card shadow'>
            <h3>{props.db.db_name}</h3>
            <div>
                <p>Project: {props.db.app_name}</p>
            </div>
            <div>
                <button
                    className='btn'
                    onClick={()=>{
                        handleGetStarted(props.db.db_name)
                    }}
                >
                    Get Started
                </button>
            </div>
        </div>
    )
}

export default DBCard