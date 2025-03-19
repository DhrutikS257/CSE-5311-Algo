FROM python:3.12-slim

WORKDIR /data_structures

COPY requirements.txt requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD bash -c "python3 --version; \
            echo -e '\nRunning ith_QuickSort:'; python3 ith_quicksort.py \
            echo -e '\nRunning Stack Tests:'; python3 test_stack.py; \
            echo -e '\nRunning Queue Tests:'; python3 test_queue.py; \
            echo -e '\nRunning Linked List Tests:'; python3 test_linked_list.py" 
