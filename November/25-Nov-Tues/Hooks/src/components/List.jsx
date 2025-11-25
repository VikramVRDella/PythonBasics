import React from 'react'

const List = () => {
    let number =[45,65,32,21]
    let fruits=['banana','mango','grapes']

    let result=fruits.map(fruit=> <h1>{fruit}</h1>)

  return (
    <div>
      {number}
      {fruits}
      {result}
    </div>
  )
}

export default List
