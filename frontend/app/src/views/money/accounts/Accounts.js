import React, { useEffect, useState } from "react";
import axios from "axios";
import {
  CCol,
  CRow,
  CTable,
  CTableBody,
  CTableDataCell,
  CTableHead,
  CTableHeaderCell,
  CTableRow,
  CBadge,
  CButton,
} from '@coreui/react'
import { useTranslation } from 'react-i18next'

const Accounts = () => {
  const apiUrl = import.meta.env.VITE_API_URL
  const { t } = useTranslation();
  const [data, setData] = useState([]);

  useEffect(() => {
    // API 호출 함수
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

    fetchData();
  }, []);

  return (
    <CRow>
      <CCol style={{ overflowX: "auto", maxWidth: "100%" }}>
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
