import React from "react";

const Home=({
    frame,language,children
})=>{
    return(
        <div>
            <h1>
                {frame}+{language} Application, this is {children}
            </h1>
        </div>
    )
}

export default Home