import React from 'react'
import { useEffect } from 'react'
import { useState } from 'react'
import axios from 'axios'

const App = () => {
  const [students,setStudents]= useState([]);
  useEffect(()=>{
    axios.get("http://127.0.0.1:8000/backend/api/")
    .then((response)=>setStudents(response.data))
    .catch((error)=>console.log(error))
  },[])
  return (
    <div>
      <h1>Message from Django</h1>
      {
        students.map((student)=>(
          <div key={student.id}>
          <p>Name : {student.name}</p>
          <p>age : {student.age}</p>
          <p>Roll no : {student.roll_no}</p>
          </div>
        ))
    }
    </div>
  )
}

export default App
