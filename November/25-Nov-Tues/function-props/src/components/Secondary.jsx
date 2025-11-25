import React from 'react'

const Secondary = ({PersonName}) => {
  return (
    <div>
      <button onClick={()=>PersonName(10,20)}>Click Me</button>
    </div>
  )
}

export default Secondary
