// CommaInput.jsx
import React, { useState } from 'react'
import { CFormInput } from '@coreui/react'

const CommaInput = ({ id, className, onChange, ...props }) => {
    const [value, setValue] = useState('')

    // 숫자 포맷팅 함수
    const formatNumberWithCommas = (inputValue) => {
        const numericValue = inputValue.replace(/,/g, '').replace(/\D/g, '') // 숫자만 남기기
        return numericValue.replace(/\B(?=(\d{3})+(?!\d))/g, ',') // 천 단위 콤마 추가
    }

    const handleChange = (e) => {
        const formattedValue = formatNumberWithCommas(e.target.value)
        setValue(formattedValue)

        // 부모 컴포넌트로 값을 전달하기 위해 콜백 호출
        if (onChange) {
            onChange(formattedValue)
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