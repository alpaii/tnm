// CommaInput.jsx
import React, { useState } from 'react'
import { CFormInput } from '@coreui/react'
import { addCommas } from '../../utils/formatUtils'

const CommaInput = ({ id, className, onChange, ...props }) => {
    const [value, setValue] = useState('')

    const handleChange = (e) => {
        const formattedValue = addCommas(e.target.value)
        setValue(formattedValue)

        // 부모 컴포넌트로 값을 전달하기 위해 콜백 호출
        if (onChange) {
            onChange(e, formattedValue)
        }
    }

    return (
        <CFormInput
            type="text"
            id={id}
            className={className}
            value={value}
            onChange={handleChange}
            {...props}
        />
    )
}

export default CommaInput