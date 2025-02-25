FROM python:3.12-slim AS builder

WORKDIR /qsort

COPY requirements.txt requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "quick_sort.py"]

FROM builder AS runner

WORKDIR /qsort

COPY --from=builder /qsort .

CMD bash -c "python3 --version && python3 quick_sort.py"