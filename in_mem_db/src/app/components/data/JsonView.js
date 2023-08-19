import React from 'react'

const JsonView = (props) => {
    const { json_data } = props

    const prettyJson = JSON.stringify(json_data, null, 2)

    return (
        <div>
            <pre>{prettyJson}</pre>
        </div>
    )
}

export default JsonView