import React, { useEffect, useRef, useState } from 'react'
import { NavLink } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'
import {
  CContainer,
  CDropdown,
  CDropdownItem,
  CDropdownMenu,
  CDropdownToggle,
  CHeader,
  CHeaderNav,
  CHeaderToggler,
  CNavLink,
  CNavItem,
  useColorModes,
} from '@coreui/react'
import CIcon from '@coreui/icons-react'
import {
  cilBell,
  cilContrast,
  cilEnvelopeOpen,
  cilList,
  cilMenu,
  cilMoon,
  cilSun,
  cifUs,
  cifFr,
  cifDe,
  cifIt,
  cifEs,
  cifKr,
  cifCn,
  cifJp,
} from '@coreui/icons'

import { AppBreadcrumb } from './index'
import { AppHeaderDropdown } from './header/index'
import { useTranslation } from "react-i18next"

const AppHeader = () => {
  const headerRef = useRef()
  const { colorMode, setColorMode } = useColorModes('coreui-free-react-admin-template-theme')

  const dispatch = useDispatch()
  const sidebarShow = useSelector((state) => state.sidebarShow)

  const { i18n } = useTranslation()

  const [selectedIcon, setSelectedIcon] = useState(cifKr) // 기본 국기: 한국
  const [selectedLanguage, setSelectedLanguage] = useState('ko') // 기본 언어: 한국어

  // 언어 변경 함수
  const changeLanguage = (lang, icon) => {
    setSelectedLanguage(lang)
    setSelectedIcon(icon)

    i18n.changeLanguage(lang)
  }

  useEffect(() => {
    document.addEventListener('scroll', () => {
      headerRef.current &&
        headerRef.current.classList.toggle('shadow-sm', document.documentElement.scrollTop > 0)
    })
  }, [])

  return (
    <CHeader position="sticky" className="mb-4 p-0" ref={headerRef}>
      <CContainer className="border-bottom px-4" fluid>
        <CHeaderToggler
          onClick={() => dispatch({ type: 'set', sidebarShow: !sidebarShow })}
          style={{ marginInlineStart: '-14px' }}
        >
          <CIcon icon={cilMenu} size="lg" />
        </CHeaderToggler>
        <CHeaderNav className="d-none d-md-flex">
          <CNavItem>
            <CNavLink to="/dashboard" as={NavLink}>
              Dashboard
            </CNavLink>
          </CNavItem>
          <CNavItem>
            <CNavLink href="#">Users</CNavLink>
          </CNavItem>
          <CNavItem>
            <CNavLink href="#">Settings</CNavLink>
          </CNavItem>
        </CHeaderNav>
        <CHeaderNav className="ms-auto">

          <CNavItem>
            <CDropdown>
              {/* 드롭다운 버튼 */}
              <CDropdownToggle className="custom-dropdown-toggle">
                <CIcon icon={selectedIcon} size="lg" />
              </CDropdownToggle>

              {/* 드롭다운 메뉴 */}
              <CDropdownMenu className="custom-dropdown-menu">
                {/* 영어 선택 */}
                <CDropdownItem onClick={() => changeLanguage("en", cifUs)}>
                  <CIcon icon={cifUs} size="lg" />
                </CDropdownItem>

                {/* 프랑스어 선택 */}
                <CDropdownItem onClick={() => changeLanguage("fr", cifFr)}>
                  <CIcon icon={cifFr} size="lg" />
                </CDropdownItem>

                {/* 독일어 선택 */}
                <CDropdownItem onClick={() => changeLanguage("de", cifDe)}>
                  <CIcon icon={cifDe} size="lg" />
                </CDropdownItem>

                {/* 이탈리아어 선택 */}
                <CDropdownItem onClick={() => changeLanguage("it", cifIt)}>
                  <CIcon icon={cifIt} size="lg" />
                </CDropdownItem>

                {/* 스페인어 선택 */}
                <CDropdownItem onClick={() => changeLanguage("es", cifEs)}>
                  <CIcon icon={cifEs} size="lg" />
                </CDropdownItem>

                {/* 한국어 선택 */}
                <CDropdownItem onClick={() => changeLanguage("ko", cifKr)}>
                  <CIcon icon={cifKr} size="lg" />
                </CDropdownItem>

                {/* 중국어 선택 */}
                <CDropdownItem onClick={() => changeLanguage("zh", cifCn)}>
                  <CIcon icon={cifCn} size="lg" />
                </CDropdownItem>

                {/* 일본어 선택 */}
                <CDropdownItem onClick={() => changeLanguage("ja", cifJp)}>
                  <CIcon icon={cifJp} size="lg" />
                </CDropdownItem>
              </CDropdownMenu>
            </CDropdown>
          </CNavItem>
          <CNavItem>
            <CNavLink href="#">
              <CIcon icon={cilBell} size="lg" />
            </CNavLink>
          </CNavItem>
          <CNavItem>
            <CNavLink href="#">
              <CIcon icon={cilList} size="lg" />
            </CNavLink>
          </CNavItem>
          <CNavItem>
            <CNavLink href="#">
              <CIcon icon={cilEnvelopeOpen} size="lg" />
            </CNavLink>
          </CNavItem>
        </CHeaderNav>
        <CHeaderNav>
          <li className="nav-item py-1">
            <div className="vr h-100 mx-2 text-body text-opacity-75"></div>
          </li>
          <CDropdown variant="nav-item" placement="bottom-end">
            <CDropdownToggle caret={false}>
              {colorMode === 'dark' ? (
                <CIcon icon={cilMoon} size="lg" />
              ) : colorMode === 'auto' ? (
                <CIcon icon={cilContrast} size="lg" />
              ) : (
                <CIcon icon={cilSun} size="lg" />
              )}
            </CDropdownToggle>
            <CDropdownMenu>
              <CDropdownItem
                active={colorMode === 'light'}
                className="d-flex align-items-center"
                as="button"
                type="button"
                onClick={() => setColorMode('light')}
              >
                <CIcon className="me-2" icon={cilSun} size="lg" /> Light
              </CDropdownItem>
              <CDropdownItem
                active={colorMode === 'dark'}
                className="d-flex align-items-center"
                as="button"
                type="button"
                onClick={() => setColorMode('dark')}
              >
                <CIcon className="me-2" icon={cilMoon} size="lg" /> Dark
              </CDropdownItem>
              <CDropdownItem
                active={colorMode === 'auto'}
                className="d-flex align-items-center"
                as="button"
                type="button"
                onClick={() => setColorMode('auto')}
              >
                <CIcon className="me-2" icon={cilContrast} size="lg" /> Auto
              </CDropdownItem>
            </CDropdownMenu>
          </CDropdown>
          <li className="nav-item py-1">
            <div className="vr h-100 mx-2 text-body text-opacity-75"></div>
          </li>
          <AppHeaderDropdown />
        </CHeaderNav>
      </CContainer>
      <CContainer className="px-4" fluid>
        <AppBreadcrumb />
      </CContainer>
    </CHeader>
  )
}

export default AppHeader
