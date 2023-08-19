import React, { useState } from 'react'

import Navigation from '../components/common/Navigation';
import { BsDatabaseAdd } from 'react-icons/bs'

import DBCard from '../components/common/DBCard';
import FormContainer from '../components/common/FormContainer';


const Home = () => {

    const [createDbForm, setCreateDbForm] = useState(false)

    const [dbCards, setDbCards] = useState([
        {
            "db_name": "test-db-1",
            "app_name": "Kanban Board"
        }, {
            "db_name": "test-db-2",
            "app_name": "Infin8 Makepolls"
        }, {
            "db_name": "test-db-3",
            "app_name": "Jira"
        }, {
            "db_name": "test-db-4",
            "app_name": "Mess Food Updates"
        }, {
            "db_name": "test-db-5",
            "app_name": "Skill Board"
        }
    ])

    function handleOpenCreateDBForm(){
        setCreateDbForm(true)
    }

    function handleCloseCreateDBForm(){
        setCreateDbForm(false)
    }

    return (
        <div>
            {
                createDbForm === true ? <FormContainer closeForm={handleCloseCreateDBForm}/> : <></>
            }
            <Navigation></Navigation>
            <div className='row'>
                <div className='column'>
                    <div
                        className='card-blank shadow'
                        style={{ cursor: "pointer" }}
                        onClick={()=>{
                            handleOpenCreateDBForm()
                        }}>
                        <div className='icon-container'>
                            <BsDatabaseAdd />
                            <div style={{ textAlign: "center", fontSize: "24px" }}>Create DB</div>
                        </div>
                    </div>
                </div>
                {
                    dbCards.map((elem, index) => {
                        return <div
                            className='column'
                            key={`elem-${index}`}>
                            <DBCard db={elem} />
                        </div>
                    })
                }
            </div>
        </div>
    )
}

export default Home