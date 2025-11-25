import React from 'react'
import Secondary from './Secondary'
const Primary = () => {
    const Change=(a,b)=>
    {
        console.log("React")
        console.log(a)
        console.log(b)
    }
    return (
        <div>
            <Secondary PersonName={Change}></Secondary>
        </div>
    )
}

export default Primary
