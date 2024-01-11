from moviepy.editor import VideoFileClip

input_file = "demonstracao.webm"
output_file = "output.gif"
start_time = 0
duration = 24
video_clip = VideoFileClip(input_file).subclip(start_time, start_time + duration)

video_clip.write_gif(output_file, fps=10)  
video_clip.close()
