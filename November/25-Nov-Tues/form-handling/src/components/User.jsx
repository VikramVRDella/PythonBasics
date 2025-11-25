import React from 'react'
import { use } from 'react'
import { useState } from 'react'

const User = () => {

  const [username, setUsername]=useState("")
  const [password, setPassword]=useState("")

  const UsernameHandler= event =>{
    setUsername(event.target.value)
  }

  const PasswordHandler= event =>{
    setPassword(event.target.value)
  }

  const UserData=(event)=>{
      event.preventDefault()

      const collected_data={
        name:username,
        pass:password
      }
      
      console.log(collected_data)
  }

  return (
    <div>
      <form onSubmit={event=> UserData(event)}>
        <label htmlFor="">Username : </label>
        {/* <input type="text" value={username} onChange={event=>console.log(event.target.value)}/> */}
        <input type="text" value={username} onChange={event=> UsernameHandler(event)}/>
        <br />
        <label htmlFor="">Password : </label>
        {/* <input type="password" value={password} onChange={event=>console.log(event.target.value)}/> */}
        <input type="password" value={password} onChange={event=>PasswordHandler(event)}/>
        <br />
        <input type="submit" />
        {/* <input type="submit" onClick={event=> UserData(event)}/> */}
        {/* <button type='submit'>Submit</button> */}
      </form>
    </div>
  )
}

export default User
