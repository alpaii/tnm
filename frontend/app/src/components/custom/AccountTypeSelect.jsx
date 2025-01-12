// components/AccountTypeSelect.jsx
import React from 'react'
import { CFormSelect } from '@coreui/react'

const AccountTypeSelect = ({ id, className, onChange, value }) => {
    const accountTypes = [
        { label: '은행', value: 'Bank' },
        { label: '신용카드', value: 'Card' },
        { label: '보증금', value: 'Deposit' },
        { label: '현금', value: 'Cash' },
        { label: '사람', value: 'Person' },
        { label: '자산', value: 'Asset' },
    ]

    return (
        <CFormSelect
            id={id}
            className={className}
            value={value}
            onChange={onChange}
        >
            {accountTypes.map((type, index) => (
                <option key={index} value={type.value} >
                    {type.label}
                </option>
            ))}
        </CFormSelect>
    )
}

export default AccountTypeSelect