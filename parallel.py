from threading import Thread, ThreadError

class Threads:
    def __init__(self):
        self.__threads = []
        
    def start(self, func, _args_: list = []) -> bool:
        # Phương thức tạo luồng mới và chạy luồng
        # func: Đối tượng mà luồng được tạo ra để áp dụng
        # _args_: Danh sách các đối số(mặc định là [])
        # Hàm trả về true nếu luồng được khởi động ngược lại trả về false
        try:
            # Tạo ra luồng cho đối tượng
            process =  Thread(target=func, args=_args_, daemon= True)
            # Bắt đâu khởi chạy luồng
            process.start()
            #
            self.__threads.append(process)
            return True
        except(ThreadError, RuntimeError) as threadStartEX:
            try:
                # Chờ kết thúc luồng 
                process.join()
            except RuntimeError:
                pass
            print(f"Threads start error: {threadStartEX}")
            return False
                        
                        
                        
    def stop(self):
        # Dừng tất cả các luồng tạo ra trong danh sách
        # Trả về true nếu dừng thành công ngược lại trả về false
        
        try:
            # Duyệt qua tất cả các luồng được tạo ra trong danh sách luồng
            for process in self.__threads:
                process.join(1)
            self.__threads.clear()
            return True
        except(ThreadError, RuntimeError) as threadsStopEx:
            print(f"Threads stop error: {threadsStopEx}")
            return False