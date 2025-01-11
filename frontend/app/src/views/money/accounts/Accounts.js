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

const Accounts = () => {
  const apiUrl = import.meta.env.VITE_API_URL

  const { t } = useTranslation();

  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const [visible, setVisible] = useState(false)

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
        <CButton color="info" size="sm" className="text-white mb-2" onClick={() => setVisible(!visible)}>추가</CButton>
        <CModal
          alignment="center"
          visible={visible}
          onClose={() => setVisible(false)}
          aria-labelledby="VerticallyCenteredExample"
        >
          <CModalHeader>
            <CModalTitle id="VerticallyCenteredExample">Modal title</CModalTitle>
          </CModalHeader>
          <CModalBody>
            <CRow className="mb-3">
              <CFormLabel htmlFor="colFormLabelSm" className="col-sm-2 col-form-label col-form-label-sm">
                Email
              </CFormLabel>
              <CCol sm={10}>
                <CFormInput
                  type="email"
                  className="form-control form-control-sm"
                  id="colFormLabelSm"
                  placeholder="col-form-label-sm"
                />
              </CCol>
            </CRow>
            <CRow className="mb-3">
              <CFormLabel htmlFor="colFormLabel" className="col-sm-2 col-form-label">
                Email
              </CFormLabel>
              <CCol sm={10}>
                <CFormInput type="email" id="colFormLabel" placeholder="col-form-label" />
              </CCol>
            </CRow>
            <CRow>
              <CFormLabel htmlFor="colFormLabelLg" className="col-sm-2 col-form-label col-form-label-lg">
                Email
              </CFormLabel>
              <CCol sm={10}>
                <CFormInput
                  type="email"
                  className="form-control form-control-lg"
                  id="colFormLabelLg"
                  placeholder="col-form-label-lg"
                />
              </CCol>
            </CRow>

          </CModalBody>
          <CModalFooter>
            <CButton color="secondary" onClick={() => setVisible(false)}>
              Close
            </CButton>
            <CButton color="primary">Save changes</CButton>
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
