import React, { useEffect, useState } from "react";
import axios from "axios";
import {
  CCard,
  CCardBody,
  CCardHeader,
  CCol,
  CRow,
  CTable,
  CTableBody,
  CTableCaption,
  CTableDataCell,
  CTableHead,
  CTableHeaderCell,
  CTableRow,
  CBadge,
  CButton,
} from '@coreui/react'
import { DocsComponents, DocsExample } from 'src/components'

const Accounts = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // API 호출 함수
    const fetchData = async () => {
      try {
        // const response = await axios.get("http://127.0.0.1:8000/api/accounts/"); // API 호출
        const response = await axios.get("http://192.168.50.183:8000/api/accounts/"); // API 호출
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
              <CTableHeaderCell scope="col" style={{ minWidth: "200px" }}>Name</CTableHeaderCell>
              <CTableHeaderCell scope="col" style={{ minWidth: "120px" }}>Balance</CTableHeaderCell>
              <CTableHeaderCell scope="col" style={{ minWidth: "250px" }}></CTableHeaderCell>
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
                <CTableDataCell className="text-end">{item.balance}</CTableDataCell>
                <CTableDataCell className="text-center"><CButton color="info" size="sm">Add</CButton></CTableDataCell>
              </CTableRow>
            ))}
          </CTableBody>
        </CTable>
      </CCol>
    </CRow>
  )
}

export default Accounts
