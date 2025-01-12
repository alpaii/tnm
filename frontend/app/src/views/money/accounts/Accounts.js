import React, { useEffect, useState } from "react";
import axios from "axios";
import {
  CCol,
  CRow,
  CTable, CTableBody, CTableDataCell, CTableHead, CTableHeaderCell, CTableRow,
  CBadge,
  CButton,
  CModal, CModalBody, CModalFooter, CModalHeader, CModalTitle,
  CFormInput, CFormLabel
} from '@coreui/react'
import { useTranslation } from 'react-i18next'
import { CommaInput, AccountTypeSelect } from '../../../components/index'
import { removeCommas } from '../../../utils/formatUtils'

const Accounts = () => {
  const apiUrl = import.meta.env.VITE_API_URL

  const { t } = useTranslation();

  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const [visible, setVisible] = useState(false)
  const [accountName, setAccountName] = useState("")
  const [accountType, setAccountType] = useState("Bank")
  const [accountBalance, setAccountBalance] = useState("")

  useEffect(() => {
    // account list
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get(apiUrl + "/api/accounts/"); // API 호출
      setData(response.data); // 데이터 설정
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  // add account
  const addAccount = async () => {
    try {
      const response = await axios.post(apiUrl + "/api/accounts/", {
        name: accountName,
        type: accountType,
        balance: removeCommas(accountBalance),
      }); // API 호출
      setVisible(false)
      fetchData();
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  const handleAccountNameChange = (e) => {
    setAccountName(e.target.value)
  }

  const handleAccountTypeChange = (e) => {
    setAccountType(e.target.value)
  }

  const handleAccountBalanceChange = (e, formattedValue) => {
    setAccountBalance(formattedValue)
  }

  return (
    <CRow>
      <CCol style={{ overflowX: "auto", maxWidth: "100%" }}>
        <CButton color="primary" size="sm" className="text-white mb-2" onClick={() => setVisible(!visible)}>추가</CButton>
        <CModal
          alignment="center"
          visible={visible}
          onClose={() => setVisible(false)}
          aria-labelledby="VerticallyCenteredExample"
        >
          <CModalHeader>
            <CModalTitle id="VerticallyCenteredExample">계좌 추가</CModalTitle>
          </CModalHeader>
          <CModalBody>
            <CRow className="mb-3">
              <CFormLabel htmlFor="accountName" className="col-sm-2 col-form-label">
                이름
              </CFormLabel>
              <CCol>
                <CFormInput type="text" id="accountName" className="col-sm-10" value={accountName} onChange={handleAccountNameChange} />
              </CCol>
            </CRow>
            <CRow className="mb-3">
              <CFormLabel htmlFor="accountType" className="col-sm-2 col-form-label">
                타입
              </CFormLabel>
              <CCol>
                <AccountTypeSelect id="accountType" className="col-sm-10" value={accountType} onChange={handleAccountTypeChange} />
              </CCol>
            </CRow>
            <CRow className="mb-3">
              <CFormLabel htmlFor="accountBalance" className="col-sm-2 col-form-label">
                잔액
              </CFormLabel>
              <CCol>
                <CommaInput id="accountBalance" className="col-sm-10" value={accountBalance} onChange={handleAccountBalanceChange} />
              </CCol>
            </CRow>
          </CModalBody>
          <CModalFooter>
            <CButton color="secondary" onClick={() => setVisible(false)}>
              닫기
            </CButton>
            <CButton color="primary" onClick={() => addAccount()}>추가</CButton>
          </CModalFooter>
        </CModal>

        <CTable bordered striped small className="table-tnm">
          <CTableHead color="info">
            <CTableRow>
              <CTableHeaderCell scope="col" style={{ minWidth: "200px" }}>{t('name')}</CTableHeaderCell>
              <CTableHeaderCell scope="col" style={{ minWidth: "120px" }}>{t('balance')}</CTableHeaderCell>
              <CTableHeaderCell scope="col" style={{ minWidth: "400px" }}></CTableHeaderCell>
            </CTableRow>
          </CTableHead>
          <CTableBody>
            {data.map((item, index) => (
              <CTableRow key={index}>
                <CTableDataCell>
                  {item.type === "Bank" && <CBadge color="primary" className="me-2">Bank</CBadge>}
                  {item.type === "Card" && <CBadge color="success" className="me-2">Card</CBadge>}
                  {item.name}
                </CTableDataCell>
                <CTableDataCell className="text-end">{item.balance.toLocaleString()}</CTableDataCell>
                <CTableDataCell className="text-center">
                  <CButton color="info" size="sm" className="text-white me-3">{t('income')}</CButton>
                  <CButton color="danger" size="sm" className="text-white me-3">{t('expense')}</CButton>
                  <CButton color="warning" size="sm" className="text-white">{t('transfer')}</CButton>
                </CTableDataCell>
              </CTableRow>
            ))}
          </CTableBody>
        </CTable>
      </CCol>
    </CRow>
  )
}

export default Accounts
