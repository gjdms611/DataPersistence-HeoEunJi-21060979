# 미션1 PoC: DataPersistence

## 목표
선택한 저장 방식으로 CRUD를 포함한 데이터 영속성(저장·불러오기) 처리가 재실행 후에도 데이터를 유지함을 검증하는 PoC를 완성한다.

## 배경
본프로젝트(SampleOrderSystem)는 시료/주문 데이터를 지속적으로 저장하고 조회해야 한다. 이를 위한 저장 방식(파일/JSON/DB 중 택1)을 개별 레포(DataPersistence-영문이름-사번)에서 먼저 검증한다. 기존 참고자료(D:\user\education\2026_CRA_AI\workspace\PoC_CRUD)를 활용할 수 있다.

## 요구사항 상세
- 저장 방식 택1: 파일 / JSON / DB (선택 방식은 TBD)
- CRUD 전체 구현:
  - Create: 신규 데이터 생성 및 저장
  - Read: 저장된 데이터 조회(전체/단건)
  - Update: 기존 데이터 수정 및 저장 반영
  - Delete: 데이터 삭제 및 저장 반영
- 재실행 후 데이터 유지(영속성) 검증: 프로그램을 종료했다가 다시 실행해도 이전에 저장한 데이터가 그대로 조회되어야 함
- 참고자료(D:\user\education\2026_CRA_AI\workspace\PoC_CRUD) 활용 가능

## 완료 기준
- [ ] Create 동작 확인(데이터 생성 후 저장소에 반영됨)
- [ ] Read 동작 확인(저장된 데이터 목록/단건 조회 가능)
- [ ] Update 동작 확인(수정 내용이 저장소에 반영됨)
- [ ] Delete 동작 확인(삭제 내용이 저장소에 반영됨)
- [ ] 프로그램 재시작 후 기존 데이터가 유지되어 조회됨을 확인

## 참고사항 및 확인 필요 사항
- 저장 방식 선택(파일/JSON/DB): TBD (사용자 확인 필요)
- 이후 DataMonitor / DummyDataGenerator / SampleOrderSystem과의 데이터 포맷 일관성 고려를 권장하나 필수는 아님
