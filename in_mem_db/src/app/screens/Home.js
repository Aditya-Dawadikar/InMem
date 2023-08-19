import React, { useState } from 'react'

import Navigation from '../components/common/Navigation';
import DBCard from '../components/common/DBCard';
import FormContainer from '../components/common/FormContainer';

import {useSelector, useDispatch} from 'react-redux'
import { openForm, closeForm } from '../redux/actions/FormActions';

import { BsDatabaseAdd } from 'react-icons/bs'

const Home = () => {

    const dispatch = useDispatch()

    const formState = useSelector((state)=>state.form)

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
        dispatch(openForm())
    }

    function handleCloseCreateDBForm(){
        dispatch(closeForm())
    }

    return (
        <div>
            {
                formState.show === true ? <FormContainer
                    closeForm={handleCloseCreateDBForm}
                    formType={"CREATE_DB"}/> : <></>
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