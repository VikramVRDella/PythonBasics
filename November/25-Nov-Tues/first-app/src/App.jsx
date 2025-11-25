import React from 'react'
import Home from './components/Home'
import { useState } from 'react';


const App = () => {
  // const language = "Javascript";

  const [language,setLanguage]=useState("Javascript")

  const Change=()=>{
    setLanguage("ReactJs")
  }
  return (
    <div>
      <Home></Home>
      <b>{language}</b>
      <br />
      <button onClick={Change}>Change Value</button>
      <br />
      <button onClick={()=>setLanguage("Python")}>Change Value</button>
      <br />
      <button>Click Me</button>
    </div>
  )
}

export default App
