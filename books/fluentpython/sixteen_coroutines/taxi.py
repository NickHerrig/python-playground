from collections import namedtuple
import queue

Event = namedtuple('Event', 'time proc action')

def compute_duration(

def taxi_process(ident, trips, start_time=0):
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trips):
        time = yield Event(time, ident, 'pick up passenger')
        time = yield Event(time, ident, 'drop off passenger')

    yield Event(time, ident, 'going home')


class Simulator:

    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time):
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)

        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print("* end of events *")
                break

            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event
            print('taxi: ', proc_id, proc_id * '   ', current_event)
            active_proc = self.procs[proc_id]
            next_time = sim_time + compute_duraction(previous_action)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)


def main():
    num_taxis = 2
    DEPARTURE_INTERVAL = 5
    taxis = {i: taxi_process(i, (i + 1) * 2, i * DEPARTURE_INTERVAL)
             for i in range(num_taxis)}

    end_time = 30
    sim = Simulator(taxis)
    sim.run(end_time)


if __name__ == '__main__':
    main()

