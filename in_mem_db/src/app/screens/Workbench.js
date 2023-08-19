import React, { useState } from 'react'

import DataViewer from './Tabs/DataViewer'
import Cache from './Tabs/Cache'
import Logs from './Tabs/Logs'
import Navigation from '../components/common/Navigation'

const Workbench = () => {
  const [tab_id, set_tab_id] = useState(0)

  function handleTabChange(index){
    set_tab_id(index)
  }

  return (
    <div>
      <Navigation></Navigation>
      <div className='tabs-header'>
        <div
          className={
            tab_id===0?'tab-item tab-item-active':'tab-item'
          }
          onClick={()=>{
            handleTabChange(0)
          }}>Data</div>
        <div
          className={
            tab_id===1?'tab-item tab-item-active':'tab-item'
          }
          onClick={()=>{
            handleTabChange(1)
          }}>Cache</div>
        <div
          className={
            tab_id===2?'tab-item tab-item-active':'tab-item'
          }
          onClick={()=>{
            handleTabChange(2)
          }}>Logs</div>
      </div>
      <br/>
      <div className='tabs-container'>
        {
          tab_id===0?<DataViewer/>:
          tab_id===1?<Cache/>:
          <Logs/>
        }
      </div>
    </div>
  )
}

export default Workbench