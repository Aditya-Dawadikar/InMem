import React from 'react'

const Navigation = () => {
  return (
    <nav className='nav'>
      <h4
        style={{display:"block", padding:"0.5em 1em"}}
        >InMemDB</h4>
      <div>
        <ul className='d-flex'>
          <li className='nav-item'><a href='/'>Home</a></li>
          <li className='nav-item'><a href='#'>FAQs</a></li>
        </ul>
      </div>
    </nav>
  )
}

export default Navigation