import React from 'react'

const App = () => {
  const PrintData=()=>
  {
    console.log("Hello")
  }
  const LogData =(a,b)=>
  {
    console.log("Clicked")
    console.log(a+b)
  }
  return (
    <div>
      <div>
        <button onClick={()=>LogData(10,20)}>ClickMe</button>
      </div>
      <div>
        <button onClick={PrintData}>ClickMe</button>
      </div>
    </div>
  )
}

export default App
