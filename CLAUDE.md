# CLAUDE.md

이 레포(`DataPersistence`) 작업 규칙.

## 목적
미션2 본프로젝트(SampleOrderSystem, 반도체 시료 생산주문관리 시스템) 전, JSON 파일 기반 CRUD 데이터 영속성(저장·불러오기)이 프로그램 재실행 후에도 유지됨을 검증하는 PoC. `REQUIREMENTS.md` 참고.

## 스택
- Python 3, 표준 라이브러리만 사용(외부 의존성 없음). 형제 PoC(ConsoleMVC, DataMonitor)와 동일한 방침.
- 참고자료: `D:\user\education\2026_CRA_AI\workspace\PoC_CRUD`
- 실행: `python crud_app.py`
- 테스트: `pytest -q`

## 저장 방식
JSON 파일 (확정, TBD 아님).

## 구조
```
storage.py     # JSON 파일 load/save
repository.py  # CRUD 로직
crud_app.py    # 콘솔 메뉴 진입점
tests/         # pytest
data/          # 실행 시 JSON 데이터 파일 저장 위치 (gitignore 대상)
```

## 완료 기준 (REQUIREMENTS.md 발췌)
- [ ] Create 동작 확인(데이터 생성 후 저장소에 반영됨)
- [ ] Read 동작 확인(저장된 데이터 목록/단건 조회 가능)
- [ ] Update 동작 확인(수정 내용이 저장소에 반영됨)
- [ ] Delete 동작 확인(삭제 내용이 저장소에 반영됨)
- [ ] 프로그램 재시작 후 기존 데이터가 유지되어 조회됨을 확인

## 금지 사항
- 미션2 본프로젝트(SampleOrderSystem) 실제 도메인(시료/주문) 코드 포함 금지
- 실제 도메인 로직 불필요 — 더미/최소 기능으로 CRUD·영속성만 검증
