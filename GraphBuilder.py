

from abc import ABC
import matplotlib.pyplot as plt
import adjustText

class GraphBuilder(ABC):

    def config_graph(self, axis_limits : list, n_traj, xlabel = "Latitude", ylabel = "Longitude", ):
        rangex = axis_limits[1] - axis_limits[0]
        rangey = axis_limits[3] - axis_limits[2]
        axis_limits[0] -= rangex*0.1
        axis_limits[1] += rangex*0.1
        axis_limits[2] -= rangey*0.1
        axis_limits[3] += rangey*0.1
        plt.axis(axis_limits)
        plt.legend(loc='lower center', ncol = n_traj, bbox_to_anchor = (0.5, 1))
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

    def plot_line(self, trajectory, line_color, line_width = 1, line_style = '-'):
        pos = trajectory.positions()
        lines = plt.plot(pos[0], pos[1], label = trajectory.id)
        plt.setp(lines, color = line_color, linewidth = line_width, linestyle = line_style)

    def plot_points(self, trajectory, point_color, marker_style, marker_size):
        pos = trajectory.positions()
        plt.scatter(pos[0], pos[1], color = point_color, marker = marker_style, s = marker_size)
    
    def plot_text(self, trajectories, key, color):
        texts = []
        for trajectory in trajectories:
            for point in trajectory.points:
                if key == 'interval temporal':
                    text = point.time
                else:
                    text = point.semantics[key]
                if trajectory.id == 'Representative Trajectory':
                    texts.append(plt.text(point.x, point.y, text, fontsize=6, c=color[1]))
                else:
                    texts.append(plt.text(point.x, point.y, text, fontsize=6, c=color[0]))
        x = adjustText.adjust_text(texts, autoalign='y', only_move={'points':'y', 'text':'y'}, 
                               force_points=0.15)#, arrowprops=dict(arrowstyle="->", color='black', lw=0.5))
        print(f"{x} interation needed")
    
    def show_plot(self):
        plt.show()
    
    def save_plot(self, filename):
        plt.savefig(filename, dpi=800, bbox_inches='tight')