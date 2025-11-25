import React from 'react'
import Secondary from './Secondary'
import { useEffect } from 'react'
import { useState } from 'react'
const Primary = () => {
    const Change=(a,b)=>
    {
        console.log("React")
        console.log(a)
        console.log(b)
    }

    const[a,setA]=useState(0)
    const[b,setB]=useState(0)

    useEffect(()=>{
        console.log("React App")
    })

    useEffect(()=>{
        console.log("Javascript")
    },[b])

    useEffect(()=>{
        console.log("Python")
    },[])
    return (
        <div>
            {a}
            <br />
            <button onClick={()=> setA(10)}>Change a</button>
            <br />
            {b}
            <br />
            <button onClick={()=> setB(20)}>Change b</button>
            <br />
            <Secondary PersonName={Change}></Secondary>
        </div>
    )
}

export default Primary
