import React from 'react'
import CreateDBForm from '../forms/CreateDBForm'

const FormContainer = (props) => {

  function handleFormInjection(formType){
    switch(formType){
      case "CREATE_DB":
        return <CreateDBForm/>
      default :
        return <></>
    }
  }

  return (
    <div>
      <div className='backdrop'>
      </div>
      <div className='form-container'>
        {
          handleFormInjection(props.formType)
        }
      </div>
    </div>
  )

}

export default FormContainer