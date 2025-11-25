import React from 'react'
import { useState } from 'react'

const Conditionals = () => {

const [user ,setUser]=useState("admin")
    let result = null
const ChangeData=()=>
{
    setUser("user")
}
    if (user === "admin")
    {
        result=<h1>You are Admin</h1>
    }
    else{
        result = <h1>You are Normal User</h1>
    }

    let a=10
    let b=a===10 ? <h1>The value of a is 10</h1> : <h1>The Value of a is unknown</h1> //ternary conditions
    let c=a===12 && <h1>React Application</h1>
  return (
    <div>
        {result}
        <br />
        {b}
        <br />
        {c}
        <br />
        <button onClick={ChangeData}>Change Value</button>
    </div>
  )
}

export default Conditionals
