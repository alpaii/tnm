// formatUtils.js

/**
 * 천단위 콤마 제거 함수
 * @param {string} numberString - 콤마가 포함된 숫자 문자열
 * @returns {number} - 콤마를 제거한 숫자
 */
export const removeCommas = (numberString) => {
    return Number(numberString.replace(/,/g, ''))
}

/**
 * 천단위 콤마 추가 함수
 * @param {string|number} number - 포맷할 숫자
 * @returns {string} - 콤마가 추가된 문자열
 */
export const addCommas = (number) => {
    const numericValue = number.toString().replace(/,/g, '')
    return numericValue.replace(/\B(?=(\d{3})+(?!\d))/g, ',')
}